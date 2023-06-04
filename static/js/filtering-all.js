function filteringAll() {
  let start_date = document.getElementById("start").value;
  let end_date = document.getElementById("end").value;
  let keyword = document.getElementById("search").value;
  let table = document.getElementById("table");
  let all_tr = table.getElementsByTagName("tr");

  keyword = keyword.toUpperCase();

  for (let i = 0; i < all_tr.length; i++) {
    let title_column = all_tr[i].getElementsByTagName("td")[1];
    let authors_column = all_tr[i].getElementsByTagName("td")[2];
    let published_column = all_tr[i].getElementsByTagName("td")[3];
    let language_column = all_tr[i].getElementsByTagName("td")[8];

    if (title_column && authors_column && published_column && language_column) {
      let title_value = title_column.textContent.toUpperCase();
      let authors_value = authors_column.textContent;
      let published_value = published_column.textContent.toUpperCase();
      let language_value = language_column.textContent.toUpperCase();

      let display = true;

      if (keyword) {
        display = (
          title_value.includes(keyword) ||
          authors_value.includes(keyword) ||
          language_value.includes(keyword)
        );
      }

      if (display) {
        if (start_date && end_date) {
          display = (published_value >= start_date && published_value <= end_date);
        } else if (start_date) {
          display = (published_value >= start_date);
        } else if (end_date) {
          display = (published_value <= end_date);
        }
      }

      all_tr[i].style.display = display ? "" : "none";
    }
  }
}
