export default function ResultViewer({ result }) {
    if (!result) return null;

    return (
        <div>
            <img
                src={`data:${result.img_type};base64,${result.annotated_image}`}
                alt="Ulcer result"
                style={{ width: "300px" }}
            />
            <h2>Dectected Ulcer Stats</h2>

            {result.ulcer_data.lenght === 0 ? (
                <p>No Ulcer Dected</p>
            ) : (
                result.ulcer_data.map((u, i) =>(
                    <div key={i} style={{ marginBottom: "8px"}}>
                        <p><b>area:</b> {u.area_px2} px²</p>
                        <p><b>Perimeter</b> {u.perimeter_px} px</p>
                    </div>
                ))
            )}
        </div>
    );
}