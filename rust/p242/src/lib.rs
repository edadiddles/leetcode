pub fn is_anagram(s: String, t: String) -> bool {
     let mut s_slice: Vec<char> = s[..].chars().collect();
     let mut t_slice: Vec<char> = t[..].chars().collect();

     if s_slice.len() != t_slice.len() {
         return false;
     }

     s_slice.sort();
     t_slice.sort();

     for (i, _) in s_slice.iter().enumerate() {
         if s_slice[i] != t_slice[i] {
             return false;
         }
     }

     true
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn case1() {
        let s = String::from("anagram");
        let t = String::from("nagaram");
        let result = is_anagram(s, t);
        assert!(result);
    }

    #[test]
    fn case2() {
        let s = String::from("rat");
        let t = String::from("car");
        let result = is_anagram(s, t);
        assert!(!result);
    }
}
