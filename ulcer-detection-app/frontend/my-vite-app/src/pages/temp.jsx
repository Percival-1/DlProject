import { useState } from "react";
import { runInference } from "../api/inference";
import ImageUploader from "../components/ImagesUploader";
import ResultViewer from "../components/ResultViewer";

export default function Home() {
    const [result, setResult] = useState(null);
    const [loading, setLoading] = useState(false);

    async function handleUpload(file) {
        setLoading(true);
        try {
            const data = await runInference(file);
            setResult(data);
        }
        finally {
            setLoading(false);
        }
    }

    return (
        <div>
            <h2>Foot Ulcer Detection</h2>
            <ImageUploader onUpload={handleUpload} />
            {loading && <p>Tunning inference...</p>}
            <ResultViewer result={result} />
        </div>
    );
}