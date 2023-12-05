/**
 * Renders the data in an HTML table.
 *
 * @param {Object} data - The data to render.
 * @returns {string|null} HTML fragment representing a table with the data or null if there is no valid data.
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