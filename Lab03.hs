data BST = Nil | Node Int BST BST

exampleTree = Node 5 (Node 3 Nil (Node 4 Nil Nil)) (Node 6 Nil Nil)

searchBST :: BST -> Int -> Bool
searchBST Nil _ = False
searchBST (Node x lBST rBST) y | x == y = True
                               | y <= x = searchBST lBST y
                               | y > x  = searchBST rBST y

inOrderBST :: BST -> [Int]
inOrderBST Nil = []
inOrderBST (Node x lBST rBST) = inOrderBST lBST ++ [x] ++ inOrderBST rBST

insertBST :: BST -> Int -> BST
insertBST Nil y = Node y Nil Nil
insertBST (Node x lBST rBST) y | y <= x = Node x (insertBST lBST y) rBST
                               | y >  x = Node x lBST (insertBST rBST y)

deleteBST :: BST -> Int -> BST
deleteBST Nil y = Nil
deleteBST (Node x Nil Nil) y = if x == y then Nil else (Node x Nil Nil)
deleteBST (Node x lBST Nil) y = if x == y then lBST else (Node x (deleteBST lBST y) Nil)
deleteBST (Node x Nil rBST) y = if x == y then rBST else (Node x Nil (deleteBST rBST y))
deleteBST (Node x lBST rBST) y | y == x = Node (smallestBST rBST) lBST (deleteBST rBST (smallestBST rBST))
                               | y <= x = Node x (deleteBST lBST y) rBST
                               | y >  x = Node x lBST (deleteBST rBST y)

smallestBST :: BST -> Int
smallestBST (Node x Nil _) = x
smallestBST (Node _ lBST _) = smallestBST lBST
