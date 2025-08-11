import argparse


def Hexdump(string):
    # Default Values___________________________________________________________________
    comparison = None  # 빈 변수 None 설정(빈 리스트, 문자열과 유사 개념)
    about_star = None
    # _________________________________________________________________________________

    for i in range(
        0, len(string), 16
    ):  # range(len(data)) 결과: 인덱스가 15개씩 중첩되어 출력됨(피라미드 형식)
        slic = string[i : i + 16]  # 16바이트씩 slicing(한 바이트 ex: 'ㄱ')
        tohex = " ".join(f"{byte:02x}" for byte in slic)  # 1개의 바이트 -> 2자리 hex로

        toascii = "".join(
            [chr(i) if 32 <= i <= 127 else "." for i in slic]
        )  # 영문만 적용됨
        # ascii 문자 범위: 32 ~ 127에 해당함

        if tohex == comparison:
            if "*" != about_star:
                print("*")
                about_star = "*"
            else:
                continue

        else:
            print(f"{i:010x}: {tohex:<48}  |{toascii}|")
            about_star = "-"

        comparison = (tohex[-3:] * 16)[
            1:
        ]  # 변수에 tohex값 저장(다음 값과 비교하기위해서)


# cmd 실행을 위한 코드

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Hexdump tool")
    parser.add_argument("file", help="파일 경로")
    args = parser.parse_args()

    with open(args.file, "br") as f:
        data = f.read()

    Hexdump(data)
