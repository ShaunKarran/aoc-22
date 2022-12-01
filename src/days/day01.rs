use crate::{Solution, SolutionPair};
use std::fs::read_to_string;

///////////////////////////////////////////////////////////////////////////////

pub fn solve() -> SolutionPair {
    let input: Vec<String> = read_to_string("input/day01.txt").unwrap()
        .lines()
        .map(str::to_string)
        .collect();

    let elves_str = input
        .split(|line| line.is_empty());
    
    let mut elves: Vec<i32> = Vec::new();
    for elf_str in elves_str {
        let elf_ints: Vec<i32> = elf_str.into_iter().map(|x| x.parse().unwrap()).collect();
        let elf_sum: i32 = elf_ints.iter().sum();
        elves.push(elf_sum);
    }
    elves.sort_by(|a, b| b.partial_cmp(a).unwrap());

    let sol1 = elves[0];
    let sol2: i32 = elves[..3].iter().sum();

    (Solution::I32(sol1), Solution::I32(sol2))
}
