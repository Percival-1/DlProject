export async function runInference(imageFile)
{
    const formData = new FormData();
    formData.append("image", imageFile);

    const response = await fetch("http://localhost:8050/infer",{
        method: "POST",
        body: formData
    });

    if (!response.ok){
        throw new Error("Inference failed");
    }

    return await response.json();
}