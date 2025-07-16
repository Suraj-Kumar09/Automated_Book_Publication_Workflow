function WriterDashboard({ chapterId }) {
  const [text, setText] = useState("");

  const handleSave = async () => {
    await fetch(`/writer/submit`, {
      method: "POST",
      body: JSON.stringify({ chapter_id: chapterId, text }),
    });
  };

  return (
    <>
      <textarea value={text} onChange={(e) => setText(e.target.value)} />
      <button onClick={handleSave}>Save</button>
    </>
  );
}
