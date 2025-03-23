pub fn merge_alternately(word1: String, word2: String) -> String {
    let w1_len = word1.len();
    let w2_len = word2.len();
   
    let l: usize;
    if w1_len > w2_len {
        l = w1_len;        
    } else {
        l = w2_len;
    }

    let mut result = String::new();
    for i in 0..l {
        if i < w1_len {
            result.push_str(&word1[i..i+1])
        }
        if i < w2_len {
            result.push_str(&word2[i..i+1])
        }
    }

    result
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn case1() {
        let word1 = String::from("abc");
        let word2 = String::from("pqr");
        let result = merge_alternately(word1, word2);

        assert_eq!(result, String::from("apbqcr"));
    }

    #[test]
    fn case2() {
        let word1 = String::from("ab");
        let word2 = String::from("pqrs");
        let result = merge_alternately(word1, word2);

        assert_eq!(result, String::from("apbqrs"));
    }

    #[test]
    fn case3() {
        let word1 = String::from("abcd");
        let word2 = String::from("pq");
        let result = merge_alternately(word1, word2);

        assert_eq!(result, String::from("apbqcd"));
    }
}
