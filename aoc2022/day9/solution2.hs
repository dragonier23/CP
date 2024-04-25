import System.IO
import Data.List
import qualified Data.Set as Set
import Data.Char

main = do
    --handle <- openFile "test2.txt" ReadMode
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
--  the head will give the position of the first 9 knots
solution :: [(Char, Int)] -> Int
solution =  Set.size . Set.fromList . tail . foldl (\(hPos:visited) (dir, x) -> reverse (actions dir x hPos) ++ visited) [[(0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)], [(0, 0)]] 

-- movement will give us direction, steps, headloc, tailloc, and returns the final location of the head and the places the tail has been 
actions :: Char -> Int -> [(Int, Int)] -> [[(Int, Int)]]
actions _ 0 knotPos = [knotPos]
actions dir x knotPos
  | dir == 'R' = [last (movement ((xh + 1, yh) : tail knotPos))] : actions dir (x-1) ((xh + 1, yh) : movement ((xh + 1, yh) : tail knotPos))
  | dir == 'L' = [last (movement ((xh - 1, yh) : tail knotPos))] : actions dir (x-1) ((xh - 1, yh) : movement ((xh - 1, yh) : tail knotPos))
  | dir == 'U' = [last (movement ((xh, yh - 1) : tail knotPos))] : actions dir (x-1) ((xh, yh - 1) : movement ((xh, yh - 1) : tail knotPos))
  | dir == 'D' = [last (movement ((xh, yh + 1) : tail knotPos))] : actions dir (x-1) ((xh, yh + 1) : movement ((xh, yh + 1) : tail knotPos))
  where (xh, yh) = head knotPos

-- i want this new movement function to take the list of things, then output the adjusted list 
movement :: [(Int, Int)] -> [(Int, Int)]
movement [x, y] = [tailMovement x y]
movement (x:y:xs) = tailMovement x y: movement (tailMovement x y : xs)

tailMovement :: (Int, Int) -> (Int, Int) -> (Int, Int)
tailMovement (xh, yh) (xt, yt)
  | xh - xt == 2 && yh - yt == 2 = (xh - 1, yh - 1)
  | xh - xt == 2 && yh - yt == (-2) = (xh - 1, yh + 1)
  | xh - xt == (-2) && yh - yt == 2 = (xh + 1, yh - 1)
  | xh - xt == (-2) && yh - yt == (-2) = (xh + 1, yh + 1)
  | xh - xt == 2 = (xh - 1, yh)
  | xh - xt == (-2) = (xh + 1, yh)
  | yh - yt == 2 = (xh, yh - 1)
  | yh - yt == (-2) = (xh, yh + 1)
  | otherwise = (xt, yt)
