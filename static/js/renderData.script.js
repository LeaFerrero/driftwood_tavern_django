/**
 * Renderiza los datos en una tabla HTML.
 *
 * @param {Object} data - Los datos a renderizar.
 * @returns {string|null} Un fragmento HTML que representa una tabla con los datos o null si no hay datos válidos.
 */
export function renderData (data)
{
    let items = null

    if(data && data.results && data.results.length > 0)
    {
        items = `
            <table>
                <thead>
                    <tr>
                        <td>Name</td>
                        <td>Effect</td>
                    </tr>
                </thead>
                <tbody>
        `;

        for (let item of data.results) 
        {
            const replaceCharacter = /[|_-]/g;
            item.desc = item.desc.replace(replaceCharacter, "");

            items += `
                <tr>
                    <td>${item.name}</td>
                    <td>${item.desc}</td>
                </tr>
            `;
        }

        items += `
                </tbody>
            </table>
        `;
    }
    else
    {
        console.error("No data to render.");
    }

    return items;
}