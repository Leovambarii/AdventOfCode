def main():
    with open('input.txt') as file:
        lines = file.read().splitlines()
        content = dict({"start":0})
        for line in lines:
            if line == "$ cd /":
                curr_dir = ["start"]
            elif line[0:7] == "$ cd ..":
                curr_dir.pop()
            elif line[0:4] == "$ cd":
                curr_dir.append("/".join([curr_dir[-1], line[5:]]))
                content[curr_dir[-1]] = 0
            elif line[0].isdigit():
                for directory in curr_dir:
                    content[directory] += int(line.split(" ")[0])
        cond_1 = filter(lambda x: x <= 1e5, content.values())
        cond_2 = filter(lambda x: x >= content["start"] - 4e7, content.values())
        print(f"1 = {sum(cond_1)}, 2 = {min(cond_2)}")


if __name__ == "__main__":
    main()