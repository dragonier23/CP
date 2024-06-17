import System.IO
import Data.List
import qualified Data.Set as Set
import Data.Char
import Data.Function

main = do
    --handle <- openFile "test1.txt" ReadMode
    handle <- openFile "problemstatement.txt" ReadMode
    contents <- hGetContents handle
    let parsed = parse contents
        max = findMax parsed + 2
        answer = solution parsed max 
        ans = Set.size answer - Set.size parsed + 1
    print ans --parsed -- max --answer -- 
    hClose handle

-- basically parse, and add all the walls to a set 
parse :: String -> Set.Set (Int, Int) --Set (Int, Int)
parse = foldl (\acc x ->
        let completed = parse' x
        in  Set.union (Set.fromList completed) acc) Set.empty .
        map (map (\x -> (read . take 3 $ x, read . drop 4 $ x)) .
        filter (\x -> not (x == "->" || x == " ")) . groupBy ((==) `on` isSpace)) .
        lines

parse' :: [(Int, Int)] -> [(Int, Int)]
parse' [(x, y)] = [(x, y)]
parse' ((x1, y1):(x2, y2):xs)
    | x1 == x2 && y1 < y2 = map (\y -> (x1, y)) [y1..y2] ++ parse' ((x2, y2):xs)
    | x1 == x2 && y1 >= y2 = map (\y -> (x1, y)) [y2..y1] ++ parse' ((x2, y2):xs)
    | y1 == y2 && x1 < x2 = map (\x -> (x, y1)) [x1..x2] ++ parse' ((x2, y2):xs)
    | otherwise = map (\x -> (x, y1)) [x2..x1] ++ parse' ((x2, y2):xs)

findMax :: Set.Set (Int, Int) -> Int
findMax = foldl (\acc (x, y) -> max y acc) 0


-- simuilate motion until there is something that escapes
solution :: Set.Set (Int, Int) -> Int -> Set.Set (Int, Int)
solution occupied max
    | finalPos == (500, 0) = occupied
    | otherwise = solution (Set.insert finalPos occupied) max
    where finalPos = falling occupied (500, 0) max


-- given the current situation, and the current location of the sand particle
-- state the end location of the sand particle
-- if the y then exceeds the limit, we return some sort of code - falling to infinity
falling :: Set.Set (Int, Int) -> (Int, Int) -> Int -> (Int, Int)
falling occupied (x, y) max
    | y+1 == max = (x, y)
    | (x, y+1) `Set.notMember` occupied = falling occupied (x, y+1) max
    | (x-1, y+1) `Set.notMember` occupied = falling occupied (x-1, y+1) max
    | (x+1, y+1) `Set.notMember` occupied = falling occupied (x+1, y+1) max
    | otherwise = (x, y)