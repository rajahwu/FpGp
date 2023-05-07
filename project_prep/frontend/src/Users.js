import { useState, useEffect } from "react";

function Users() {
  const [users, setUsers] = useState({});

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await fetch("/api/users/");
        const data = await response.json();
        setUsers(data);
      } catch (error) {
        console.log("Error fetching data: ", error);
      }
    };

    fetchData();
  }, []);

  return (
    <>
      <h1>Users</h1>
      <ul style={{ listStyle: "none" }}>
        {users.users?.map((user) => {
          return (
            <div key={user.id}>
              <li>Id {user.id}</li>
              <li>
                {user.firstName} {user.lastName}
              </li>
              <li>{user.email}</li>
            </div>
          );
        })}
      </ul>
    </>
  );
}

export default Users;
