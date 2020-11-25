import React, { useState } from "react";
import ScriptTag from 'react-script-tag';




const ExternalApi = () => {
  const [message, setMessage] = useState("");

  return (
    <div>
      <h1>View General Weather for you area</h1>
      <p>
       Type in your city and you will get weather genrated from the local area weather station
        <br />
        <strong>Not as accurate as weather Pi</strong>.
      </p>
      <html>
        <iframe src= "http://localhost:3001/"></iframe>
      </html>

      

      </div>

    
        
  );

  };

export default ExternalApi;
