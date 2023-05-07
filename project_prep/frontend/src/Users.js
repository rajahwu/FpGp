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

  console.log(users);
  return <h1>Users</h1>;
}

export default Users;
