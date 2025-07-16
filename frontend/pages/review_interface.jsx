function ReviewInterface({ chapterId }) {
  const [comments, setComments] = useState("");
  const [rating, setRating] = useState(0);

  const handleReview = async () => {
    await fetch(`/reviewer/submit`, {
      method: "POST",
      body: JSON.stringify({ chapter_id: chapterId, comments, rating }),
    });
  };

  return (
    <>
      <textarea value={comments} onChange={(e) => setComments(e.target.value)} />
      <input type="number" value={rating} onChange={(e) => setRating(e.target.value)} />
      <button onClick={handleReview}>Submit Review</button>
    </>
  );
}
