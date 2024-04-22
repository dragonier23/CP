{-# OPTIONS_GHC -Wno-unrecognised-pragmas #-}
{-# HLINT ignore "Eta reduce" #-}
import System.IO
import Data.List
import qualified Data.Set as Set 
import Data.Char 

main = do 
    handlestack <- openFile "problemstatementstack.txt" ReadMode --"teststack.txt" ReadMode -- 
    handlemoves <- openFile "problemstatementmoves.txt" ReadMode --"testmoves.txt" ReadMode -- 
    contentstack <- hGetContents handlestack
    contentmoves <- hGetContents handlemoves  
    let parsedContentStack = parseStack contentstack
        parsedContentMoves = parseMoves contentmoves 
        answer = solution parsedContentStack parsedContentMoves
    print answer -- parsedContentMoves --  
    hClose handlemoves
    hClose handlestack 

parseStack :: String -> [String]
parseStack = map (dropWhile (==' ')) . transpose' . init . map parse' . lines

parse' :: String -> [Char]
parse' [] = []
parse' xs = xs !! 1 : parse' (drop 4 xs)

transpose' :: [String] -> [String]
transpose' ([]:_) = []
transpose' x = map head x : transpose' (map tail x)

parseMoves :: String -> [(Int, Int, Int)]
parseMoves = map (\line -> 
    let [_, x, _, y, _, z] = words line 
    in (read x, read y - 1, read z - 1)) . lines 


solution :: [String] -> [(Int, Int, Int)] -> String
solution stack moves = map head $ foldl (\acc (num, from, to) -> 
    movement acc num from to (take num (acc !! from))) stack moves

movement :: [String] -> Int -> Int -> Int -> String -> [String] 
movement [] _ _ _ _ = []
movement (x:xs) num 0 to moved  = drop num x : movement xs num (-1) (to-1) moved
movement (x:xs) num from 0 moved  = (moved ++ x) : movement xs num (from-1) (-1) moved
movement (x:xs) num from to moved  = x : movement xs num (from-1) (to-1) moved