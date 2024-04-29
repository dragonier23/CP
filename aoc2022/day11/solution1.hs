import System.IO
import Data.List
import qualified Data.Set as Set
import Data.Char

main = do
    --handle <- openFile "test1.txt" ReadMode
    handle <- openFile "problemstatement.txt" ReadMode
    contents <- hGetContents handle
    let parsedActions = parse contents
        initState = parse'' . lines $ contents
        postActions = solution initState . repeat' 20 $ parsedActions
        [x, y] = take 2 . reverse . sort $ (postActions !! 1)
        answer = x * y
    print answer 
    hClose handle

parse :: String -> [((String, Int), Int, Int, Int)]
parse = parse' . lines

parse' :: [String] -> [((String, Int), Int, Int, Int)]
parse' [] = []
parse' (x:xs)
    | null x = parse' xs
parse' (_:_:a:b:c:d:xs) =
  let [symbol, val] = drop 4 . words $ a
      opr = if val == "old" then "**" else symbol
      value = if val == "old" then 2 else read val
  in ((opr, value), read . last . words $ b, read . last . words $ c, read . last . words $ d) : parse' xs

parse'' :: [String] -> [[Int]]
parse'' [] = []
parse'' (x:xs)
  | null x = parse'' xs
parse'' (_:x:_:_:_:_:xs) = initState : parse'' xs
  where tmp = drop 2 . words $ x
        initState = map (\y -> if last y == ',' then read . init $ y else read y) tmp

repeat' :: Int -> [a] -> [a]
repeat' 0 _ = []
repeat' x xs = xs ++ repeat' (x-1) xs

-- our solution will do a fold, with acc being the current state, and moves feeding the current monkey's decision matrix
solution :: [[Int]] ->  [((String, Int), Int, Int, Int)] -> [[Int]]
solution states = foldl (\([turn]:inspectionCount:xs) x ->
  let items = xs !! turn -- extracting the current monkey's items
      updatedInspectionCount = take turn inspectionCount ++ [(inspectionCount !! turn) + length items] ++ drop (turn + 1) inspectionCount 
      processItems = map (`processing` x) items -- deciding what to do with the items (of the form [(end val, next)])
      finalState = foldl (\acc (endVal, next) -> insert' next endVal acc) (take turn xs ++ [[]] ++ drop (turn + 1) xs) processItems
  in [(turn + 1) `mod` length states] : updatedInspectionCount : finalState) ([0]:replicate (length states) 0:states)

-- we can figure out whose turn it is by looking at how many moves we have 
insert' :: Int -> Int -> [[Int]] -> [[Int]]
insert' monkey val xs = take monkey xs ++ [val : xs !! monkey] ++ drop (monkey + 1) xs

processing :: Int -> ((String, Int), Int, Int, Int) -> (Int, Int)
processing item (("**", 2), test, pass, fail) =
  let final = (item ^ 2) `div` 3
  in if (final `mod` test) == 0 then (final, pass) else (final, fail)
processing item (("*", val), test, pass, fail) =
  let final = (item * val) `div` 3
  in if (final `mod` test) == 0 then (final, pass) else (final, fail)
processing item (("+", val), test, pass, fail) =
  let final = (item + val) `div` 3
  in if (final `mod` test) == 0 then (final, pass) else (final, fail)
