# creating a chess engine 

import chess 
import numpy as np

class State(object):
    def __init__(self, board=None):
        if board is None:
            self.board = chess.Board()
        else:
            self.board = board
        self.bstate = np.zeros(64, np.uint8)

    def edges(self):
        return list(self.board.legal_moves)

    def key(self): # change this later to some other name 
        return (self.board.board_fen(), self.board.turn, self.board.castling_rights, self.board.ep_square)

    def serialize(self):
        import numpy as np
        #print('this is the serialize function called')
        assert self.board.is_valid()

        bstate = np.zeros(64, np.uint8)
        #print('bstate is : ', bstate)

        for i in range(64):
            pp = self.board.piece_at(i)
            #print('pp( board piece ) is : ', pp)
            #input('press enter to continue')
            if pp is not None:
                # print(i, pp.symbol())
                bstate[i] = {"P": 1, "N": 2, "B": 3, "R": 4, "Q": 5, "K": 6, \
                            "p": 9, "n":10, "b":11, "r":12, "q":13, "k": 14}[pp.symbol()]
                
            # print('#################')    
            # print('bstate is : ', bstate)

        self.bstate = bstate
        print(np.reshape(self.bstate, (8,8)))
        return bstate
    
    def render(self):
        # visualize the board as 8,8 matrix
        #reshape as 8,8 and print
        print(np.reshape(self.bstate, (8,8)))

    def value(self):
        return 0

if __name__=="__main__":
    print(chess.Board().is_valid())
    print(type(chess.Board()))
    state = State()
    print(state.board)
    print(state.board.is_valid())
    # board = State()
    # print(board.edges())
    # print(board.key())
    # print(board.serialize())
    # print(board.)
    # print(board.is_valid())
    # print('hi')
    # print(board.legal_moves)
    # print(board.board_fen())
    # print(f'the turn in of : {board.turn}')
    # print(board.is_checkmate())
    # print(board.is_game_over())
    # print(board.is_stalemate())
    # print(board.is_check())
    # print(board.is_fivefold_repetition())
    # print(board.is_seventyfive_moves())
    # print(board.is_insufficient_material())
    # print(board.is_variant_end())
    # print(board.is_valid())
    # print(board.is_capture(chess.Move.from_uci("a2a3")))
    # print(board.is_castling(chess.Move.from_uci("e1g1")))
    # print(board.is_kingside_castling(chess.Move.from_uci("e1g1")))
    # print(board.is_queenside_castling(chess.Move.from_uci("e1c1")))
    # print(board.is_en_passant(chess.Move.from_uci("a5b6")))
    # print(board.is_promotion(chess.Move.from_uci("a7a8q")))
    # print(board.is_nullmove(chess.Move.null()))
    # print(board.is_variant_win())
    # print(board.is_variant_loss())
    # print(board.is_variant_draw())
    # print(board.is_variant_end())
    # print(board.is_variant_win())
    # print(board.is_variant_loss())
    # print(board.is_variant_draw())
    # print(board.is_variant_end())
    # print(board.is_variant_win())
    # print(board.is_variant_loss())
    # print(board.is_variant_draw())
    # print(board.is_variant_end())
    # print(board.is_variant_win())
    # print(board.is_variant_loss())
    # print(board.is_variant_draw())
    # print(board.is_variant_end())
    # print(board.is_variant_win())
    # print(board.is_variant_loss())
    # print(board.is_variant_draw())
    # print(board.is_variant_end())
    # print(board.is_variant_win())
    # print(board.is_variant_loss())
    # print(board.is_variant_draw())
    # print(board.is_variant_end())
    # print(board.is_variant_win())
    # print(board.is_variant_loss())
    # print(board.is_variant_draw())
    # print(board.is_variant_end())
    # print(board.is_variant_win())
    # print(board.is_variant_loss())
    # print(board.is_variant_draw())
    # print(board.is_variant_end())

    # print(board.has_kingside_castling_rights(chess.WHITE))
    # print(board.has_kingside_castling_rights(chess.BLACK))
    # print(board.has_queenside_castling_rights(chess.WHITE))
    # print(board.has_queenside_castling_rights(chess.BLACK))    
