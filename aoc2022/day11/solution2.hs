import System.IO
import Data.List
import qualified Data.Set as Set
import Data.Char

main = do
    handle <- openFile "test1.txt" ReadMode
    --handle <- openFile "problemstatement.txt" ReadMode
    contents <- hGetContents handle
    let parsedActions = parse contents
        initState = parse'' . lines $ contents
        postActions = solution initState . repeat' 10000 $ parsedActions
        [x, y] = take 2 . reverse . sort $ (postActions !! 1)
        answer = x * y
    print answer 
    hClose handle

parse :: String -> [((String, Integer), Integer, Integer, Integer)]
parse = parse' . lines

parse' :: [String] -> [((String, Integer), Integer, Integer, Integer)]
parse' [] = []
parse' (x:xs)
    | null x = parse' xs
parse' (_:_:a:b:c:d:xs) =
  let [symbol, val] = drop 4 . words $ a
      opr = if val == "old" then "**" else symbol
      value = if val == "old" then 2 else read val
  in ((opr, value), read . last . words $ b, read . last . words $ c, read . last . words $ d) : parse' xs

parse'' :: [String] -> [[Integer]]
parse'' [] = []
parse'' (x:xs)
  | null x = parse'' xs
parse'' (_:x:_:_:_:_:xs) = initState : parse'' xs
  where tmp = drop 2 . words $ x
        initState = map (\y -> if last y == ',' then read . init $ y else read y) tmp

repeat' :: Integer -> [a] -> [a]
repeat' 0 _ = []
repeat' x xs = xs ++ repeat' (x-1) xs

-- our solution will do a fold, with acc being the current state, and moves feeding the current monkey's decision matrix
solution :: [[Integer]] ->  [((String, Integer), Integer, Integer, Integer)] -> [[Integer]]
solution states = foldl' (\([turn]:inspectionCount:xs) x ->
  let items = xs !! fromIntegral turn -- extracting the current monkey's items
      updatedInspectionCount = take (fromIntegral turn) inspectionCount ++ [(inspectionCount !! fromIntegral turn) + fromIntegral (length items)] ++ drop (fromIntegral turn + 1) inspectionCount
      processItems = map (`processing` x) items -- deciding what to do with the items (of the form [(end val, next)])
      finalState = foldl' (\acc (endVal, next) -> insert' next endVal acc) (take (fromIntegral turn) xs ++ [[]] ++ drop (fromIntegral turn + 1) xs) processItems
  in [(turn + 1) `mod` fromIntegral (length states)] : updatedInspectionCount : finalState) ([0]:replicate (length states) 0:states)

-- we can figure out whose turn it is by looking at how many moves we have 
insert' :: Integer -> Integer -> [[Integer]] -> [[Integer]]
insert' monkey val xs = take (fromIntegral monkey) xs ++ [val : xs !! fromIntegral monkey] ++ drop (fromIntegral monkey + 1) xs

processing :: Integer -> ((String, Integer), Integer, Integer, Integer) -> (Integer, Integer)
processing item (("**", 2), test, pass, fail) =
  let final = (item ^ 2)
  in if (final `mod` test) == 0 then (final, pass) else (final, fail)
processing item (("*", val), test, pass, fail) =
  let final = (item * val)
  in if (final `mod` test) == 0 then (final, pass) else (final, fail)
processing item (("+", val), test, pass, fail) =
  let final = (item + val)
  in if (final `mod` test) == 0 then (final, pass) else (final, fail)
