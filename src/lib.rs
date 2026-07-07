//! Native CPF/CNPJ validation for the `pycpfcnpj` package.
//!
//! Behaviour matches the pure-Python core in `pycpfcnpj/_core.py`:
//! punctuation `. - /` is stripped, all-identical inputs are rejected, and the
//! CNPJ path accepts the 2026 alphanumeric format (letters map to `ord - 48`).

use pyo3::prelude::*;

const CPF_W1: [u32; 9] = [10, 9, 8, 7, 6, 5, 4, 3, 2];
const CPF_W2: [u32; 10] = [11, 10, 9, 8, 7, 6, 5, 4, 3, 2];
const CNPJ_W1: [u32; 12] = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2];
const CNPJ_W2: [u32; 13] = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2];

#[inline]
fn check_digit(vals: &[u32], weights: &[u32]) -> u32 {
    let total: u32 = vals.iter().zip(weights).map(|(v, w)| v * w).sum();
    let rest = total % 11;
    if rest < 2 {
        0
    } else {
        11 - rest
    }
}

#[inline]
fn valid_cpf(s: &[u8]) -> bool {
    let first = s[0];
    let mut all_same = true;
    let mut vals = [0u32; 11];
    for (i, &b) in s.iter().enumerate() {
        if !b.is_ascii_digit() {
            return false;
        }
        if b != first {
            all_same = false;
        }
        vals[i] = (b - 48) as u32;
    }
    if all_same {
        return false;
    }
    if vals[9] != check_digit(&vals[..9], &CPF_W1) {
        return false;
    }
    vals[10] == check_digit(&vals[..10], &CPF_W2)
}

#[inline]
fn valid_cnpj(s: &[u8]) -> bool {
    let first = s[0].to_ascii_uppercase();
    let mut all_same = true;
    let mut vals = [0u32; 14];
    for (i, &b0) in s.iter().enumerate() {
        let b = b0.to_ascii_uppercase();
        if b.is_ascii_digit() || b.is_ascii_uppercase() {
            vals[i] = (b - 48) as u32;
        } else {
            return false;
        }
        if b != first {
            all_same = false;
        }
    }
    if all_same {
        return false;
    }
    // The two check digits must always be numeric, even in the alphanumeric format.
    if !s[12].is_ascii_digit() || !s[13].is_ascii_digit() {
        return false;
    }
    if vals[12] != check_digit(&vals[..12], &CNPJ_W1) {
        return false;
    }
    vals[13] == check_digit(&vals[..13], &CNPJ_W2)
}

/// Strip `. - /`, keeping other bytes, into a fixed buffer. Returns the length,
/// or `None` if the cleaned input would not fit (i.e. it cannot be a document).
#[inline]
fn clean(doc: &str, buf: &mut [u8; 32]) -> Option<usize> {
    let mut n = 0usize;
    for &b in doc.as_bytes() {
        match b {
            b'.' | b'-' | b'/' => continue,
            _ => {
                if n >= buf.len() {
                    return None;
                }
                buf[n] = b;
                n += 1;
            }
        }
    }
    Some(n)
}

#[pyfunction]
fn validate_cpf(cpf_number: &str) -> bool {
    let mut buf = [0u8; 32];
    match clean(cpf_number, &mut buf) {
        Some(11) => valid_cpf(&buf[..11]),
        _ => false,
    }
}

#[pyfunction]
fn validate_cnpj(cnpj_number: &str) -> bool {
    let mut buf = [0u8; 32];
    match clean(cnpj_number, &mut buf) {
        Some(14) => valid_cnpj(&buf[..14]),
        _ => false,
    }
}

/// Facade: dispatch to CPF (11) or CNPJ (14) based on cleaned length.
#[pyfunction]
fn validate(number: &str) -> bool {
    let mut buf = [0u8; 32];
    match clean(number, &mut buf) {
        Some(11) => valid_cpf(&buf[..11]),
        Some(14) => valid_cnpj(&buf[..14]),
        _ => false,
    }
}

#[pymodule]
fn _speedups(m: &Bound<'_, PyModule>) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(validate_cpf, m)?)?;
    m.add_function(wrap_pyfunction!(validate_cnpj, m)?)?;
    m.add_function(wrap_pyfunction!(validate, m)?)?;
    Ok(())
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn cpf_valid_plain_and_masked() {
        assert!(validate_cpf("11144477735"));
        assert!(validate_cpf("111.444.777-35"));
    }

    #[test]
    fn cpf_invalid_dv() {
        assert!(!validate_cpf("11144477736"));
    }

    #[test]
    fn cpf_rejects_all_same_wrong_size_and_non_digits() {
        for d in 0..=9 {
            assert!(!validate_cpf(&d.to_string().repeat(11)));
        }
        assert!(!validate_cpf("111444777")); // too short
        assert!(!validate_cpf("111444A7735")); // letter
        assert!(!validate_cpf("*55759997&9")); // special chars
    }

    #[test]
    fn cnpj_valid_numeric_and_masked() {
        assert!(validate_cnpj("11444777000161"));
        assert!(validate_cnpj("11.444.777/0001-61"));
    }

    #[test]
    fn cnpj_valid_alphanumeric_2026() {
        assert!(validate_cnpj("12ABC34501DE35"));
        assert!(validate_cnpj("12abc34501de35")); // lowercase normalizes
    }

    #[test]
    fn cnpj_invalid_cases() {
        assert!(!validate_cnpj("11444777000162")); // wrong dv
        assert!(!validate_cnpj("12ABC34501DE36")); // wrong alphanumeric dv
        assert!(!validate_cnpj("12ABC34501DEA5")); // letter in verifier
        assert!(!validate_cnpj("12ABC34501DE@5")); // special char
        assert!(!validate_cnpj("12ABC34501DE3")); // too short
        for d in 0..=9 {
            assert!(!validate_cnpj(&d.to_string().repeat(14)));
        }
    }

    #[test]
    fn facade_dispatches_by_length() {
        assert!(validate("11144477735")); // cpf
        assert!(validate("11444777000161")); // cnpj
        assert!(validate("12ABC34501DE35")); // alphanumeric cnpj
        assert!(!validate("111444777")); // neither length
        assert!(!validate("")); // empty
    }

    #[test]
    fn check_digit_boundaries() {
        // rest < 2 -> 0
        assert_eq!(check_digit(&[0], &[1]), 0);
        assert_eq!(check_digit(&[1], &[1]), 0); // rest 1 -> 0
                                                // rest >= 2 -> 11 - rest
        assert_eq!(check_digit(&[2], &[1]), 9); // rest 2 -> 9
    }
}
