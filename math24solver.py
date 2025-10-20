import sys
import json

def main():
    try:
        if len(sys.argv) != 5:
            raise ValueError("Exactly four positive integer arguments are required.")
            
        num1 = sys.argv[1]
        num2 = sys.argv[2]
        num3 = sys.argv[3]
        num4 = sys.argv[4]

        nums = [num1,num2,num3,num4]
        ops = ['+', '-', '*', '/']
        resultset = set()
        for a in range(4):
            for b in range(4):
                for c in range(4):
                    for d in range(4):
                        for e in range(4):
                            for f in range(4):
                                for g in range(4):
                                    if a != c and a != e and a != g and c != e and c != g and e != g:
                                        estr = '(((' + nums[a] + ops[b] + nums[c] + ')' + ops[d] + nums[e]+ ')'  + ops[f] + nums[g] + ')'
                                        val = eval(estr)
                                        if val == 24:
                                            resultset.add(estr)
        
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
