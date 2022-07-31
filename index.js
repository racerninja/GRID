const express = require('express')
const app = express()
const Sneaker = require('./Sneaker')
const path = require('path')
const ejsMate = require('ejs-mate');

app.engine('ejs', ejsMate);
app.set('views', path.join(__dirname, 'views'))
app.set('view engine', 'ejs')
app.use(express.json())
app.use(express.static("public"));

const URL = "mongodb+srv://manavgrover:sexaddict69@cluster0.nxg7w.mongodb.net/Matrix?retryWrites=true&w=majority";
const mongoose = require('mongoose');
mongoose.connect(URL, {useNewUrlParser: true, useUnifiedTopology: true});
var db = mongoose.connection;

db.on("error", console.error.bind(console, 'MongoDB connection error:'));
db.once("open", () => {
    console.log("Database connected");
})

app.get('/', async (req, res) => {
    const data = await Sneaker.find({})
    res.render('index', {data : data})
})

app.get('/product/:id', async (req, res) => {
    const id = req.params;
    const data = await Sneaker.find({});
    res.render('product', {data : data, id})
})

const port = process.env.PORT || 5000;
app.listen(port, ()=> {
    console.log(`litening port ${port}`);
})

