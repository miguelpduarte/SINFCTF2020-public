const form = document.querySelector("form.search");
const input = document.querySelector("input.searchTerm");
const output = document.querySelector("#output");

const query_to_xml = (data) => "" +
`<?xml version="1.0" encoding="UTF-8"?>
    <root>
	<query>
	    ${data}
	</query>
    </root>
`

form.addEventListener('submit', async (e) => {
    e.preventDefault();
    const search_query = input.value;
    const data = query_to_xml(search_query);

    const res = await fetch("/multimedia-me.php", {
	method: 'POST',
	headers: {
	    'Content-Type': 'text/xml; charset=utf-8',
	},
	body: data,
    });

    const html_response = await res.text();
    output.innerHTML = html_response;
});
