import game1
import game2
import view
import logger

def run():
    mode = view.choose_mode()
    if mode == 'крестики нолики':
        result = game1.run_game()
        view.show_results(result)
        logger.log_result(result)
    if mode == 'конфеты':
        result = game2.run_game()
        view.show_results(result)
        logger.log_result(result)    