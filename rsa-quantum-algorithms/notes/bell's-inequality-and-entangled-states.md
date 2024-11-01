# Bell's Inequality and Entangled States

Recall the lecture on Alice and Bob on different planets, trying to "win" a game by receiving bits and sending back bits. They can only win if the AND of their input bits a and b = the XOR of their response bits, x and y.

Bell's Inequality states that, assuming classical information, no matter what strategy they employ, their probability of winning the game is <= 0.75.

If they use quantum information, this can be increase to 0.8. How?

Assume that Bob and Alice share an entangled state of two qubits, represented by 1/sqrt(2)(|00> + |11>)

If either of them receive a 1, they apply a rotation of pi/8 (Alice) or -pi/8 (Bob) and measure the qubit and send back the result.

If they receive a 0, they do not apply anything to the qubit, and they simply measure it and send back the result. 

Case 1: Both receive 0; chance of winning is 1
Case 2: Either one receives a 1, but not both; chance of winning is about 0.85
Case 3: Both receive a 1; chance of winning is 0.5