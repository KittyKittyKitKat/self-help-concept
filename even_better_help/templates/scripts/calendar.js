function hello() {
    console.log("hi");
}

//TO-DO: move globals up here
const month_arr = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'];
const month_len = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31];


function generate_grid() {
    let days = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"];
    let header = document.createElement("div");
    header.classList.add("row");
    for (let i = 0; i < 7; i++) {
        let header_col = document.createElement("div");
        header_col.classList.add("col", "grid-fix", "px-1");
        header_col.innerHTML = days[i];
        header.appendChild(header_col);
    }
    //TO-DO: clean this up

    let count = 0;
    let id = 0;
    let dummy = false;

    document.getElementById("grid-anchor").appendChild(header)
    for (let i = 0; i < 5; i++) { // need five rows to contain all possible days
        let new_row = document.createElement("div");
        new_row.classList.add("row");
        for (let j = 0; j < 7; j++) { // need seven days per week (duh)
            let new_col = document.createElement("div");
            new_col.classList.add("col", "grid-fix", "px-1");
            if (count >= window.start_day && count < window.last_day + window.start_day) {
                dummy = false;
                id++;
            } else {
                dummy = true;
            }
            const day1 = "hello hewoo this is my day 1 and this should be extracted from a json";

            count++;
            btn = generate_day(new_col, id, dummy);
            new_col.appendChild(btn);
            new_row.appendChild(new_col);
        }
        document.getElementById("grid-anchor").appendChild(new_row);
    }
}

function update_dates() {
    let date = new Date();
    window.year = date.getFullYear();
    window.month = date.getMonth();
    document.getElementById("month_entry").innerHTML = month_arr[window.month];
    document.getElementById("year_entry").innerHTML = window.year;
    let start_date = new Date(window.year, window.month, 1);
    window.start_day = start_date.getDay();
    window.last_day = month_len[window.month];

}

function generate_day(col, id, dummy) {
    let btn = document.createElement("button");
    btn.classList.add("btn", "btn-dark", "my-1", "btn-day", "btn-circle");
    btn.innerHTML = id;
    btn.setAttribute("data-bs-target", "#staticBackdrop");
    btn.setAttribute("data-bs-toggle", "modal");
    btn.addEventListener("click", () => {
        update_day(id);
    });
    btn.id = id - 1;
    if (dummy) {
        btn.disabled = true
        btn.innerHTML = ":3";
    }

    return btn;
}

function update_day(id) {
    console.log(entry_arr[id]);
    document.getElementById("journal_entry").value = entry_arr[id];
}
    
hello();