import Head from "next/head";

export default function Home() {
  return (
    <>
      <div className="bg-dark text-white min-vh-100 d-flex flex-column justify-content-center align-items-center">
        <div
          className="jumbotron text-center my-5"
          style={{ maxWidth: "50%", margin: "auto" }}
        >
          <h1 className="display-1">CRAMMASTER.AI</h1>
          <h6 className="display-7 text-end">Created By: Abhishek</h6>
        </div>
      </div>
    </>
  );
}
