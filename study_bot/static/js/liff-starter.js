let CUR_CONTAINER = "form-container";
const LIFF_ID = "1655195434-krMxK6vy";
const API = {
  addRecord: "https://study-bot-creek0810.herokuapp.com/records/",
  recentRecords: "https://study-bot-creek0810.herokuapp.com/records/recent",
}

function toggleContainer(elId) {
  const curEl = document.getElementById(elId);
  if (curEl !== null) {
    if (curEl.classList.contains("hidden")) {
      curEl.classList.remove("hidden");
    } else {
      curEl.classList.add("hidden");
    }
  }
}

function showContainer(containerId) {
  // init
  if (CUR_CONTAINER === null) {
    CUR_CONTAINER = containerId;
    toggleContainer(containerId);
    return;
  }
  // hidden last container and show current container
  toggleContainer(CUR_CONTAINER);
  CUR_CONTAINER = containerId;
  toggleContainer(CUR_CONTAINER);
}

function register() {
  showContainer("form-container");
}

async function renderChart() {
  showContainer("chart-container");
  // get data
  const profile = await liff.getProfile()
  const result = await fetch(`${API.recentRecords}/${profile.userId}`);
  const data = await result.json();
  // show
  ctx = document.getElementById("chart");
  var myLineChart = new Chart(ctx, {
    type: 'line',
    data: {
      labels: data.labels,
      datasets: [{
          label: '# of Problems',
          data: data.data,
          borderColor: "#4CC0C0",
          backgroundColor: 'rgba(0, 0, 0, 0)',
          borderWidth: 2
      }]
  },
    //options: options
  });
}

async function submit() {
  const profile = await liff.getProfile()
  const result = {
    userId: profile.userId,
    date: new Date().toISOString(),
    number: document.getElementById("number").value,
    type: document.getElementById("type").value
  };
  const rv = await fetch(API.addRecord, {
    method: "POST",
    body: JSON.stringify(result),
    headers: {
      'Content-Type': 'application/json'
    },
  });

  // TODO: register success animation
  if(rv.status === 409) {
    document.getElementById("message-body").innerText = "Duplicate problem";
  } else if (rv.status === 200) {
    document.getElementById("message-body").innerText = "Success";
  } else {
    document.getElementById("message-body").innerText = "Error";
  }
  $('#message-modal').modal('show')
}

function initLiff() {
  liff.init({
    liffId: LIFF_ID
  });
}

function init() {
  initLiff()
  // register event
  document.getElementById("register").addEventListener("click", register);
  document.getElementById("render-chart").addEventListener("click", renderChart);
  document.getElementById("submit").addEventListener("click", submit);
}

window.addEventListener('load', init);
