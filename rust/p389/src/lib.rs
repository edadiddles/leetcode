
pub fn find_the_difference(s: String, t: String) -> char {
    let mut s_slice: Vec<char> = s[..].chars().collect();
    let mut t_slice: Vec<char> = t[..].chars().collect();
    s_slice.sort_by(|a,b| b.cmp(a));
    t_slice.sort_by(|a,b| b.cmp(a));

    let mut diff: char = t_slice[t_slice.len()-1];
    let mut i = 0;
    for c in s_slice.iter() {
        if *c != t_slice[i] {
            diff = t_slice[i];
            break;
        }
        i += 1;
    }

    diff
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn case1() {
        let s = String::from("abcd");
        let t = String::from("abcde");
        let result = find_the_difference(s, t);
        assert_eq!(result, 'e');
    }

    #[test]
    fn case2() {
        let s = String::from("");
        let t = String::from("y");
        let result = find_the_difference(s, t);
        assert_eq!(result, 'y');
    }

    #[test]
    fn case3() {
        let s = String::from("edcba");
        let t = String::from("edcfba");
        let result = find_the_difference(s, t);
        assert_eq!(result, 'f');
    }
}
