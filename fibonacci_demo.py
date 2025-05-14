def fibonacci_debug(n, depth=0):
	print("  " * depth + f"fibonacci({n}) called")
    
	if n == 0:
		print("  " * depth + "return 0")
		return 0
	elif n == 1:
		print("  " * depth + "return 1")
		return 1
    
	val = fibonacci_debug(n - 1, depth + 1) + fibonacci_debug(n - 2, depth + 1)
	print("  " * depth + f"return {val} for fibonacci({n})")
	return val

if __name__ == "__main__":
	fibonacci_debug(5)