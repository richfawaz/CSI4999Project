import React from "react";

const logo = "https://cdn.auth0.com/blog/auth0-react-sample/assets/logo.png";

const Hero = () => (
  <div className="text-center hero">
    <div><h1><i class="fas fa-cloud-sun-rain"></i></h1></div>
    <h1 className="mb-4">Weather PI</h1>
    <p className="lead">
   Your personal weather station, powered by{" "}
      <a
        target="_blank"
        rel="noopener noreferrer"
        href="https://www.raspberrypi.org/"
      >
        Raspberry pi
      </a>
    </p>
  </div>
);

export default Hero;
