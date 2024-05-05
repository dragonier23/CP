import System.IO
import Data.List
import qualified Data.Set as Set
import Data.Char

main = do
    --handle <- openFile "test1.txt" ReadMode
    handle <- openFile "problemstatement.txt" ReadMode
    contents <- hGetContents handle
    let parsedActions = parse contents
        modulo = parse''' parsedActions
        initState = parse'' (lines contents) modulo
        postActions = solution initState modulo (repeat' 10000 parsedActions)
        [x, y] = take 2 . reverse . sort $ head (postActions !! 1)
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

parse'' :: [String] -> [Int] -> [[[Int]]]
parse'' [] _ = []
parse'' (x:xs) modulo
  | null x = parse'' xs modulo
parse'' (_:x:_:_:_:_:xs) modulo = initStateMod : parse'' xs modulo
  where tmp = drop 2 . words $ x
        initState = map (\y -> if last y == ',' then read . init $ y else read y) tmp
        initStateMod = map (\z -> map (\a -> z `mod` a) modulo) initState

parse''' :: [((String, Int), Int, Int, Int)] -> [Int]
parse''' [] = []
parse''' ((_, x, _, _):xs) = x:parse''' xs

repeat' :: Int -> [a] -> [a]
repeat' 0 _ = []
repeat' x xs = xs ++ repeat' (x-1) xs

-- our solution will do a fold, with acc being the current state, and moves feeding the current monkey's decision matrix
solution :: [[[Int]]] -> [Int] -> [((String, Int), Int, Int, Int)] -> [[[Int]]]
solution states modulo = foldl (\([[turn]]:[inspectionCount]:xs) x ->
  let items = xs !! turn -- extracting the current monkey's items
      updatedInspectionCount = take turn inspectionCount ++ [(inspectionCount !! turn) + length items] ++ drop (turn + 1) inspectionCount
      processItems = map (\y -> processing y modulo turn x) items -- deciding what to do with the items (of the form [(end val, next)])
      finalState = foldl (\acc (endVal, next) -> insert' next endVal acc) (take turn xs ++ [[]] ++ drop (turn + 1) xs) processItems
  in [[(turn + 1) `mod` length states]] : [updatedInspectionCount] : finalState) ([[0]]:[replicate (length states) 0]:states)

-- we can figure out whose turn it is by looking at how many moves we have 
insert' :: Int -> [Int] -> [[[Int]]] -> [[[Int]]]
insert' monkey val xs = take monkey xs ++ [val : xs !! monkey] ++ drop (monkey + 1) xs

-- processing needs to take the int, in the form of the mods, take the mods themselves, and the decision matrix, and the turn 
processing :: [Int] -> [Int] -> Int -> ((String, Int), Int, Int, Int) -> ([Int], Int)
processing item modulo turn (("**", 2), test, pass, fail) =
  let final = zipWith (\x y -> (x ^ 2) `mod` y) item modulo
  in if (final !! turn) == 0 then (final, pass) else (final, fail)
processing item modulo turn (("*", val), test, pass, fail) =
  let final = zipWith (\x y -> (x * val) `mod` y) item modulo
  in if (final !! turn) == 0 then (final, pass) else (final, fail)
processing item modulo turn (("+", val), test, pass, fail) =
  let final = zipWith (\x y -> (x + val) `mod` y) item modulo
  in if (final !! turn) == 0 then (final, pass) else (final, fail)
