function UploadURLPage() {
  const [url, setUrl] = useState("");

  const handleSubmit = async () => {
    await fetch("/scrape", {
      method: "POST",
      body: JSON.stringify({ url }),
    });
  };

  return (
    <>
      <input value={url} onChange={(e) => setUrl(e.target.value)} />
      <button onClick={handleSubmit}>Submit</button>
    </>
  );
}
