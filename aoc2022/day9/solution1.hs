import System.IO
import Data.List
import qualified Data.Set as Set
import Data.Char

main = do
    --handle <- openFile "test1.txt" ReadMode
    handle <- openFile "problemstatement.txt" ReadMode --"test1.txt" ReadMode --
    contents <- hGetContents handle
    let parsedContents = parse contents
        answer = solution parsedContents
    print answer --parsedContents --answer
    hClose handle

--parsed :: String -> [Int]
parse :: String -> [(Char, Int)]
parse = map (\x -> let [dir:xs, steps] = words x in (dir, read steps)) . lines

-- we want this to give a list of the visited tail locations. 
-- head of the returned list should give the head's current location, and the rest is the visited places of the tail 
solution :: [(Char, Int)] -> Int
solution = Set.size . Set.fromList . tail . foldl (\(hPos:tPos:visited) (dir, x) -> (reverse . movement dir x hPos $ tPos) ++ (tPos:visited)) [(0, 0), (0, 0)]

-- movement will give us direction, steps, headloc, tailloc, and returns the final location of the head and the places the tail has been 
movement :: Char -> Int -> (Int, Int) -> (Int, Int) -> [(Int, Int)]
movement _ 0 hPos _ = [hPos]
movement dir x (xh, yh) (xt, yt)
  | dir == 'R' = tailMovement (xh + 1, yh) (xt, yt) : movement dir (x-1) (xh + 1, yh) (tailMovement (xh + 1, yh) (xt, yt))
  | dir == 'L' = tailMovement (xh - 1, yh) (xt, yt) : movement dir (x-1) (xh - 1, yh) (tailMovement (xh - 1, yh) (xt, yt))
  | dir == 'U' = tailMovement (xh, yh - 1) (xt, yt) : movement dir (x-1) (xh, yh - 1) (tailMovement (xh, yh - 1) (xt, yt))
  | dir == 'D' = tailMovement (xh, yh + 1) (xt, yt) : movement dir (x-1) (xh, yh + 1) (tailMovement (xh, yh + 1) (xt, yt))

tailMovement :: (Int, Int) -> (Int, Int) -> (Int, Int)
tailMovement (xh, yh) (xt, yt)
  | xh - xt == 2 = (xh - 1, yh)
  | xh - xt == (-2) = (xh + 1, yh)
  | yh - yt == 2 = (xh, yh - 1)
  | yh - yt == (-2) = (xh, yh + 1)
  | otherwise = (xt, yt)
