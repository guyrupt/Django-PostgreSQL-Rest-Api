import { Select } from 'antd';
import 'antd/dist/antd.css';
import axios from 'axios';
import { useEffect, useState } from 'react';

const { Option } = Select;

const Tags = ({ setTag, setCheck , company, location, level}) => {

    const [tags, setTags] = useState([])
    let url = 'http://127.0.0.1:8000/companytag/'+ company + '/' + location + '/' + level
    //let url = str.replace(/%20/g, " ")
    useEffect(() => {
      console.log(url)
        axios.get(url)
        .then((res) => { 
          console.log(res.data)
          setTags(res.data)
        })
        .catch((error) => { console.log(error) })
    },[url])

    const onChange = (value) => {
        console.log(`selected ${value}`);
        setTag(value)
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
        {tags.map((tag)=>{
            return <Option value={tag['tag_name']}>{tag['tag_name']}</Option>
        })}
        </Select>
      );

}



export default Tags