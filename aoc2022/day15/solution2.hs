{-# OPTIONS_GHC -Wno-unrecognised-pragmas #-}
{-# HLINT ignore "Use map once" #-}
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
        (_, x, y) = solution' . solution $ parsed
        answer = x * 4000000 + y
    print answer -- present) -- parsed --
    hClose handle

parse :: String -> [(Int, Int, Int, Int)] 
parse = map ((\x -> (read . drop 2 . init $ (x !! 4), read . drop 2 . init $ (x !! 6), read . drop 2 . init $ (x !! 16), read . drop 2 $ (x !! 18))) . groupBy ((==) `on` isSpace)) .
        lines

-- takes row, and b/s coordinates 
-- in solution 2 case, if returned start not <= 0 then we know its that row 
solution :: [(Int, Int, Int, Int)] -> [Int]
solution input =  map (\(_, start, _) -> if start > 0 then start - 1 else -1) . map (\x -> settle . sort . foldl (\acc (sx, sy, bx, by) ->
                let dist = abs (sx - bx) + abs (sy - by)
                    remainder = dist - abs (x - sy)
                in  if remainder > 0 then (sx - remainder, sx + remainder):acc else acc) [] $ input) $ [0..4000000]

settle :: [(Int, Int)] -> (Int, Int, Int)
settle ((sx, sy):xs) = foldl (\(count, start, end) (nextStart, nextEnd) -> if nextStart <= end then (if nextEnd <= end then (count, start, end) else (count + nextEnd - end, start, nextEnd)) else (count + nextEnd - nextStart + 1, nextStart, nextEnd)) (sy - sx + 1, sx, sy) xs

solution' :: [Int] -> (Int, Int, Int)
solution' = foldl (\(acc, maxX, maxY) int -> if int > maxX then (acc + 1, int, acc) else (acc + 1, maxX, maxY)) (0, -1, -1)