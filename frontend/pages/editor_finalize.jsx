function FinalEditor({ chapterId }) {
  const [finalText, setFinalText] = useState("");

  const finalize = async () => {
    await fetch(`/editor/finalize`, {
      method: "POST",
      body: JSON.stringify({ chapter_id: chapterId, final_text: finalText }),
    });
  };

  return (
    <>
      <textarea value={finalText} onChange={(e) => setFinalText(e.target.value)} />
      <button onClick={finalize}>Finalize</button>
    </>
  );
}
