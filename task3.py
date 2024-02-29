#Personal property of Owais Ali

# Create a script that reads the access log from a file. The name of the file is provided as an argument. An output of the script should provide the total number of different User Agents and then provide statistics with the number of requests from each of them.

def read_access_log():
    file_path = "/Users/oali/Downloads/Python-Tasks/Task1/access.log.5"
    user_agents = {}
    total_requests = 0

    try:
        with open(file_path, 'r') as file:
            for line in file:
                parts = line.split('"')
                if len(parts) > 5:
                    user_agent = parts[5]
                    if user_agent in user_agents:
                        user_agents[user_agent] += 1
                    else:
                        user_agents[user_agent] = 1
                    total_requests += 1
    except FileNotFoundError:
        print("Error: File not found.")
        return None

    return user_agents, total_requests

def main():
    user_agents, total_requests = read_access_log()

    if user_agents is not None:
        print("Total number of different User Agents:", len(user_agents))
        print("Total number of requests:", total_requests)
        print("\nStatistics:")
        for user_agent, count in user_agents.items():
            print(f"{user_agent}: {count} requests")

if __name__ == "__main__":
    main()
