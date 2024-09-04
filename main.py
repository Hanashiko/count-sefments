def countSegments(s: str) -> int:
    return len(s.split()) 

def main() -> None:
    print(countSegments("Hello, my name is John"))
    print(countSegments("Hello"))
    
if __name__ == "__main__":
    main()