prices :: [Int]
prices = [1,5,8,9,10,17,17,20,24,30]

maxPrice :: [Int]
maxPrice = [1,5,8,10,13,17,18,22,25,30]

rodCuttingTest :: (Int -> [Int] -> Int) -> Bool
rodCuttingTest f = and [ maxPrice!!(n-1) == (f n prices) | n <- [1..10] ]

-- RodCutting takes in a Size of Rod, a list of sizes and prices and returns
--      the maximum price that can be achieved.
naiveRodCutting :: Int -> [Int] -> Int
naiveRodCutting 0 _  = 0
naiveRodCutting n ps = maximum [ ps!!(i-1) + (naiveRodCutting (n-i) ps) | i <- [1..n] ]

memoizedRodCutting :: Int -> [Int] -> Int
memoizedRodCutting n ps = 
