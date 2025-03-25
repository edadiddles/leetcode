pub fn str_str(haystack: String, needle: String) -> i32 {
    if haystack.len() < needle.len() {
        return -1
    }

    let h_slice: Vec<char> = haystack[..].chars().collect();
    let n_slice: Vec<char> = needle[..].chars().collect();

    let mut res: i32 = -1;
    for (i, _) in h_slice.iter().enumerate() {
        let mut is_not_matched = false;

        if n_slice.len() > h_slice.len()-i {
            return -1
        }

        for (j, _) in n_slice.iter().enumerate() {
            if &n_slice[j..j+1] != &h_slice[j+i..j+i+1] {
                is_not_matched = true;
                break;
            }    
        }

        if !is_not_matched {
            res = i as i32;
            break;
        }
    }

    res
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn case1() {
        let str1 = String::from("sadbutsad");
        let str2 = String::from("sad");
        let result = str_str(str1, str2);
        assert_eq!(result, 0);
    }

    #[test]
    fn case2() {
        let str1 = String::from("leetcode");
        let str2 = String::from("leeto");
        let result = str_str(str1, str2);
        assert_eq!(result, -1);
    }

    #[test]
    fn case3() {
        let str1 = String::from("aaa");
        let str2 = String::from("aaaa");
        let result = str_str(str1, str2);
        assert_eq!(result, -1);
    }

    #[test]
    fn case4() {
        let str1 = String::from("mississippi");
        let str2 = String::from("issipi");
        let result = str_str(str1, str2);
        assert_eq!(result, -1);
    }
}
