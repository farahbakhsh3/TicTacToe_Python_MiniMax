/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package tictactoe_minimax;

import java.util.ArrayList;
import java.util.Random;


public class TicTacToe_MiniMax {

    static class Move {

        int row;
        int col;
        int val;
    }

    static Random rand = new Random();

    public static final int ONE_PLAYER = 0;
    public static final int TWO_PLAYER = 1;
    public static final int GAME_LEVEL_BEGINNER = 50;
    public static final int GAME_LEVEL_EASY = 60;
    public static final int GAME_LEVEL_NORMAL = 85;
    public static final int GAME_LEVEL_HARD = 100;
    final static int RED_CODE_HUMAN = 1;
    final static int RED_CODE_HUMAN_DB_SCORE_idx = 0;
    final static int YELLOW_CODE_AI = 2;
    final static int YELLOW_CODE_AI_DB_SCORE_idx = 2;
    final static int NOT_PLAYED = 0;
    final static int DRAW = 0;
    final static int DRAW_DB_SCORE_idx = 1;
    final static int NO_WINNER_DRAW = -1;
    final static int BOARD_SIZE = 5;
    final static int GOAL_SIZE = 4;
    final static int SCORE_MAX = 1000;
    final static int SCORE_MIN = -1000;
    final static int SCORE_PLUS = 50;
    final static int SCORE_MINUS = -50;
    final static int SCORE_ZERO = DRAW;
    final static int N_NEIGHBOR_MAX = GOAL_SIZE / 2 + GOAL_SIZE % 2;
    static int game_level;
    static int[][] gameBoard = new int[BOARD_SIZE][BOARD_SIZE];
    static int play_type = ONE_PLAYER;
    static int activePlayer = RED_CODE_HUMAN;
    static int score = NO_WINNER_DRAW;
    static boolean AI_turn = false;
    static int DEPTH = -1;
    static int idxDepth;

    public static int NOT_PLAYED_counter(int[][] board) {
        int cnt = 0;
        for (int row = 0; row < BOARD_SIZE; row++) {
            for (int col = 0; col < BOARD_SIZE; col++) {
                if (board[row][col] == NOT_PLAYED) {
                    cnt++;
                }
            }
        }

        return cnt;
    }

    public static Boolean isMovesLeft(int[][] board) {
        for (int row = 0; row < BOARD_SIZE; row++) {
            for (int col = 0; col < BOARD_SIZE; col++) {
                if (board[row][col] == NOT_PLAYED) {
                    return true;
                }
            }
        }

        return false;
    }

    public static int evaluateBoard(int[][] board, int GOAL_SIZE, boolean recursive) {
        if (recursive) {
            if (GOAL_SIZE < 3) {
                return SCORE_ZERO;
            }
        }

        boolean human = true;
        boolean AI = true;

        for (int row = 0; row < BOARD_SIZE; row++) {
            for (int col = 0; col < BOARD_SIZE - GOAL_SIZE + 1; col++) {
                human = true;
                AI = true;
                for (int chk = 0; chk < GOAL_SIZE; chk++) {
                    if (board[row][col + chk] != RED_CODE_HUMAN) {
                        human = false;
                    }
                    if (board[row][col + chk] != YELLOW_CODE_AI) {
                        AI = false;
                    }
                }
                if (human) {
                    return SCORE_MINUS;
                }
                if (AI) {
                    return SCORE_PLUS;
                }
            }
        }

        for (int col = 0; col < BOARD_SIZE; col++) {
            for (int row = 0; row < BOARD_SIZE - GOAL_SIZE + 1; row++) {
                human = true;
                AI = true;
                for (int chk = 0; chk < GOAL_SIZE; chk++) {
                    if (board[row + chk][col] != RED_CODE_HUMAN) {
                        human = false;
                    }
                    if (board[row + chk][col] != YELLOW_CODE_AI) {
                        AI = false;
                    }
                }
                if (human) {
                    return SCORE_MINUS;
                }
                if (AI) {
                    return SCORE_PLUS;
                }
            }
        }

        for (int row = 0; row < BOARD_SIZE - GOAL_SIZE + 1; row++) {
            for (int col = 0; col < BOARD_SIZE - GOAL_SIZE + 1; col++) {
                human = true;
                AI = true;
                for (int chk = 0; chk < GOAL_SIZE; chk++) {
                    if (board[row + chk][col + chk] != RED_CODE_HUMAN) {
                        human = false;
                    }
                    if (board[row + chk][col + chk] != YELLOW_CODE_AI) {
                        AI = false;
                    }
                }
                if (human) {
                    return SCORE_MINUS;
                }
                if (AI) {
                    return SCORE_PLUS;
                }
            }
        }

        for (int row = 0; row < BOARD_SIZE - GOAL_SIZE + 1; row++) {
            for (int col = GOAL_SIZE - 1; col < BOARD_SIZE; col++) {
                human = true;
                AI = true;
                for (int chk = 0; chk < GOAL_SIZE; chk++) {
                    if (board[row + chk][col - chk] != RED_CODE_HUMAN) {
                        human = false;
                    }
                    if (board[row + chk][col - chk] != YELLOW_CODE_AI) {
                        AI = false;
                    }
                }
                if (human) {
                    return SCORE_MINUS;
                }
                if (AI) {
                    return SCORE_PLUS;
                }
            }
        }
        if (recursive) {
            return evaluateBoard(board, GOAL_SIZE - 1, true) / 2;
        }
        return SCORE_ZERO;
    }

    public static int minimax(int[][] board, int depth, Boolean isMax, int alpha, int beta) {

        int score = evaluateBoard(board, GOAL_SIZE, true);

//        idxMove++;
        idxDepth = Math.max(idxDepth, depth);

        if (score == SCORE_PLUS) {
//            idxGameOver++;
            return score - depth;
        }
        if (score == SCORE_MINUS) {
//            idxGameOver++;
            return score + depth;
        }
        if (!isMovesLeft(board) || (depth > DEPTH)) {
//            idxGameOver++;
            return score;
        }

        if (((depth > DEPTH) && (DEPTH > 0))) {
            return score;
        }

        if (isMax) {
            int best = SCORE_MIN;

            for (int row = 0; row < BOARD_SIZE; row++) {
                for (int col = 0; col < BOARD_SIZE; col++) {
                    if (board[row][col] == NOT_PLAYED && isNeighborN(board, row, col, N_NEIGHBOR_MAX)) {
                        board[row][col] = YELLOW_CODE_AI;

                        int val = minimax(board, depth + 1, false, alpha, beta);
                        best = Math.max(best, val);
                        alpha = Math.max(alpha, best);
                        board[row][col] = NOT_PLAYED;

                        if (beta <= alpha) {
                            break;
                        }
                    }
                }
            }
            return best;
        } else {
            int best = SCORE_MAX;

            for (int row = 0; row < BOARD_SIZE; row++) {
                for (int col = 0; col < BOARD_SIZE; col++) {
                    if (board[row][col] == NOT_PLAYED && isNeighborN(board, row, col, N_NEIGHBOR_MAX)) {
                        board[row][col] = RED_CODE_HUMAN;

                        int val = minimax(board, depth + 1, true, alpha, beta);
                        best = Math.min(best, val);
                        beta = Math.min(beta, best);
                        board[row][col] = NOT_PLAYED;

                        if (beta <= alpha) {
                            break;
                        }
                    }
                }
            }
            return best;
        }
    }

    public static int CalcDepth(int[][] board) {
        int n = NOT_PLAYED_counter(board);
        if (n >= 20) {
            return 4;
        }
        if (n >= 15) {
            return 5;
        }
        if (n >= 10) {
            return 6;
        }
        return 99;
    }

    public static boolean isNeighborN(int[][] board, int row, int col, int N_NEIGHBOR) {
        for (int i = -N_NEIGHBOR; i <= N_NEIGHBOR; i++) {
            if (row + i >= 0 && row + i < BOARD_SIZE) {
                for (int j = -N_NEIGHBOR; j <= N_NEIGHBOR; j++) {
                    if (col + j >= 0 && col + j < BOARD_SIZE) {
                        if (i == 0 || j == 0 || Math.abs(i) == Math.abs(j)) {
                            if (board[row + i][col + j] != NOT_PLAYED) {
                                return true;
                            }
                        }
                    }
                }
            }
        }
        return false;
    }

    public static Move findBestMove(int[][] board) {
        Move bestMove = new Move();
        bestMove.row = -1;
        bestMove.col = -1;
        bestMove.val = SCORE_MIN;

        ArrayList<int[]> lst = new ArrayList<>();

        for (int row = 0; row < BOARD_SIZE; row++) {
            for (int col = 0; col < BOARD_SIZE; col++) {
                DEPTH = CalcDepth(board);
                if (board[row][col] == NOT_PLAYED && isNeighborN(board, row, col, N_NEIGHBOR_MAX)) {
                    board[row][col] = YELLOW_CODE_AI;

                    int moveVal = minimax(board, 0, false, SCORE_MIN, SCORE_MAX);

                    board[row][col] = NOT_PLAYED;

                    if (moveVal > bestMove.val) {
                        bestMove.row = row;
                        bestMove.col = col;
                        bestMove.val = moveVal;
                        int[] x = {bestMove.row, bestMove.col, bestMove.val};
                        lst.clear();
                        lst.add(x);
                    } else if (moveVal == bestMove.val) {
                        bestMove.row = row;
                        bestMove.col = col;
                        bestMove.val = moveVal;
                        int[] x = {bestMove.row, bestMove.col, bestMove.val};
                        lst.add(x);
                    }

                    String m = row + "," + col + ":" + (row * BOARD_SIZE + col) + "\t"
                            + "\t depth: " + idxDepth + "\t Score: " + moveVal;
                    System.out.println(m);
                }
            }
        }

        int r = rand.nextInt(lst.size());
        bestMove.row = lst.get(r)[0];
        bestMove.col = lst.get(r)[1];
        bestMove.val = lst.get(r)[2];

        String m = "ROW: " + bestMove.row + " COL: " + bestMove.col;
        System.out.println(m);

        return bestMove;
    }

    static void print_board(int board[][]) {
        for (int row = 0; row < BOARD_SIZE; row++) {
            for (int col = 0; col < BOARD_SIZE; col++) {
                System.out.printf("%s ", (board[row][col] == 0 ? "_" : board[row][col]));
            }
            System.out.printf("\n");
        }
//        System.out.printf("idxDepth:%d---s:%d\n", idxDepth, evaluateBoard(board, GOAL_SIZE, false));
        System.out.println("");
    }
   // Driver code
    public static void main(String[] args) {
        int board[][]
                = {
                    {2, 1, 1, 1, 2},
                    {0, 1, 1, 2, 1},
                    {1, 2, 1, 2, 0},
                    {2, 1, 2, 2, 2},
                    {0, 2, 0, 1, 0},};

        print_board(board);
        Move bestMove = findBestMove(board);
//        for (int row = 0; row < BOARD_SIZE; row++) {
//            for (int col = 0; col < BOARD_SIZE; col++) {
//                if (isNPath(board, row, col)) {
//                    System.out.printf("row: %d \t col: %d \n",row, col);
//                }
//            }
//        }
        System.out.printf("\n\nThe Optimal Move is :\n");
        System.out.printf("ROW: %d COL: %d\n\n", bestMove.row, bestMove.col);
//        System.out.println("" + evaluate(board, GOAL_SIZE));
    }
}
