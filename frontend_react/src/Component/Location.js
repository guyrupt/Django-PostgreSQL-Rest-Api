import { Select } from 'antd';
import 'antd/dist/antd.css';
import axios from 'axios';
import { useEffect, useState } from 'react';

const { Option } = Select;

const Locations = ({ setLocation, setCheck, company}) => {

    const [locations, setLocations] = useState([])
    console.log(company)
    let url = 'http://127.0.0.1:8000/companyloc/'+ company
    //let url = str.replace(" ", /%20/g)
    console.log(url)
    useEffect(() => {
        console.log(url)
        axios.get(url)
        .then((res) => { 
          //console.log(res.data);
          setLocations(res.data)
          //console.log(locations);
        })
        .catch((error) => { console.log(error) })
    },[url])

    const onChange = (value) => {
        console.log(`selected ${value}`);
        //console.log(locations);
        setLocation(value)
        setCheck(false)
      }
      
    const onSearch = (val) => {
        console.log('search:', val);
      }
      
      return(
        <Select
          showSearch
          style={{ width: 200 }}
          defaultValue={'All'}
          onChange={onChange}
          onSearch={onSearch}
          filterOption={(input, option) =>
            option.children.toLowerCase().indexOf(input.toLowerCase()) >= 0
          }
        >
        <Option value={null}>{"All"}</Option>
        {locations.map((location)=>{
            return <Option value={location['location_name']}>{location['location_name']}</Option>
        })}
        </Select>
      );

}



export default Locations