const mongoose = require('mongoose');
const Schema = mongoose.Schema;

const productSchema = new Schema({
    product_brand : String, 
    product_name : String,
    product_link : String,
    product_des : String,
    price : String,
    image_links : [{type:String}],
    insta_links : [{type:String}],
    flipkart_link : String,
    color : [{type:Number}]
})

module.exports = mongoose.model('Sneaker', productSchema);
