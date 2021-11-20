import { Select } from 'antd';
import 'antd/dist/antd.css';
import axios from 'axios';
import { useEffect, useState } from 'react';

const { Option } = Select;

const Levels = ({ setLevel, setCheck , company, location}) => {

    const [levels, setLevels] = useState([])
    console.log(company)
    console.log(location)
    let url = 'http://127.0.0.1:8000/companylevel/'+ company +'/' + location
    //let url = str.replace(/%20/g, " ")
    console.log(url)
    useEffect(() => {
        console.log(url)
        axios.get(url)
        .then((res) => { 
          console.log(res.data);
          setLevels(res.data)
          //console.log(levels);
        })
        .catch((error) => { console.log(error) })
    },[url])

    const onChange = (value) => {
        console.log(`selected ${value}`);
        setLevel(value)
        setCheck(false)
      }
      
    const onSearch = (val) => {
        console.log('search:', val);
      }
      
      return(
        <Select
          showSearch
          style={{ width: 200 }}
          defaultValue={null}
          onChange={onChange}
          onSearch={onSearch}
          filterOption={(input, option) =>
            option.children.toLowerCase().indexOf(input.toLowerCase()) >= 0
          }
        >
        <Option value={null}>{"All"}</Option>
        {levels.map((level)=>{
            return <Option value={level['level_name']}>{level['level_name']}</Option>
        })}
        </Select>
        
      );

}



export default Levels