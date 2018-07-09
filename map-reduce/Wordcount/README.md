### Map/Reduce - Wordcount with streaming, using Python code.

#### Task
Running wordcount_mapper.py and wordcount_reducer.py on testfile1 and testfile2

#### Solution
- mapper
  - Get word
  - Emit `<word> < 1>`

- reducer
  - Get next <word><value>
  - If `<word>` is same as previous word
    - add `<value>` to count
  - else
    - emit `<word> < count>`
    - set count to 0

#### Result
- with default numReduceTasks, result in wordcount_num_default_output.txt
- with numReduceTasks=0 (no reducers), result in wordcount_num0_output.txt, we can see that words and counts are not accumulated.
