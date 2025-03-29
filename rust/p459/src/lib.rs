pub fn repeated_substring_pattern(s: String) -> bool {
    let n = s.len();
    for i in 1..=n/2 {
        if n%i != 0 {
            continue;
        }
        let mut is_matched = true;
        for j in 1..n/i {
            if s[0..i] != s[i*j..i*j+i] {
                is_matched = false;
                break;
            }
        }

        if is_matched {
            return true;
        }
    }
            
    false
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn case1() {
        let s = String::from("abab");
        let result = repeated_substring_pattern(s);
        assert_eq!(result, true);
    }

    #[test]
    fn case2() {
        let s = String::from("aba");
        let result = repeated_substring_pattern(s);
        assert_eq!(result, false);
    }

    #[test]
    fn case3() {
        let s = String::from("abcabcabcabc");
        let result = repeated_substring_pattern(s);
        assert_eq!(result, true);
    }

    #[test]
    fn case4() {
        let s = String::from("bb");
        let result = repeated_substring_pattern(s);
        assert_eq!(result, true);
    }

}
