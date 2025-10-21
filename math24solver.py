import sys
import json
import itertools

def main():
    try:
        if len(sys.argv) != 5:
            raise ValueError("Exactly four integer arguments are required.")
            
        nums = [sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4]]
        ops = ['+', '-', '*', '/']
        resultset = set()
        
        for n1, n2, n3, n4 in itertools.permutations(nums):
            for op1, op2, op3 in itertools.product(ops, repeat=3):
                estr = f'((({n1}{op1}{n2}){op2}{n3}){op3}{n4})'
                try:
                    val = eval(estr)
                    if val == 24:
                        resultset.add(estr)
                except ZeroDivisionError:                   
                    continue

        if not resultset:
            resultset.add("There are no solutions.")
        
        output_list = list(resultset)
        print(json.dumps(output_list))
        sys.stdout.flush()

    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
