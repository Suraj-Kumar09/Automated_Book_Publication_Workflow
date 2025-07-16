function VersionViewer({ chapterId }) {
  const [versions, setVersions] = useState([]);

  useEffect(() => {
    fetch(`/versions/${chapterId}`).then(res => res.json()).then(setVersions);
  }, []);

  return (
    <>
      {versions.map((v, i) => (
        <div key={i}>
          <h3>Version {i + 1}</h3>
          <p>{v.text}</p>
        </div>
      ))}
    </>
  );
}


# this is Comment